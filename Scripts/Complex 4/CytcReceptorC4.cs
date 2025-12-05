using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CytcReceptorC4 : MonoBehaviour
{
    private Vector2 forceDir;
    private Rigidbody2D cytochromeBody;
    private SpriteRenderer cytochromeSprite;
    private Oxidator oxidator;
    public float forceMag = 10;
    public float reactionRadius = 3;
    public Sprite cytcOxSprite;
    public Sprite cytcRedSprite;

    void Awake()
    {
        oxidator = GetComponentInParent<Oxidator>();        
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (!collision.CompareTag("cytochromec")) return;

        cytochromeBody = collision.gameObject.GetComponent<Rigidbody2D>();
        cytochromeSprite = collision.gameObject.GetComponent<SpriteRenderer>();

        forceDir = (transform.position - cytochromeBody.transform.position).normalized;
        if (cytochromeSprite.sprite == cytcRedSprite)
        {
            cytochromeSprite.sprite = cytcOxSprite;
            oxidator.oxygenElectrons += 1;
        }
        else if (cytochromeSprite.sprite == cytcOxSprite)
        {
            cytochromeBody.AddForce(forceDir * -forceMag, ForceMode2D.Force);
        }
    }
}
