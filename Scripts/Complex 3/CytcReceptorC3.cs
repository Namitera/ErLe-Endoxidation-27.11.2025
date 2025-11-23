using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CytcReceptorC3 : MonoBehaviour
{
    private Vector2 forceDir;
    private Rigidbody2D cytochromeBody;
    private SpriteRenderer cytochromeSprite;
    private QCycleHub qCycleHub;
    public float forceMag = 10;
    public float reactionRadius = 3;
    public Sprite cytcOxSprite;
    public Sprite cytcRedSprite;

    void Awake()
    {
        qCycleHub = GetComponentInParent<QCycleHub>();        
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (!collision.CompareTag("cytochromec")) return;

        cytochromeBody = collision.gameObject.GetComponent<Rigidbody2D>();
        cytochromeSprite = collision.gameObject.GetComponent<SpriteRenderer>();

        forceDir = (transform.position - cytochromeBody.transform.position).normalized;
        if (cytochromeSprite.sprite == cytcOxSprite && qCycleHub.cytcElectrons > 0)
        {
            cytochromeSprite.sprite = cytcRedSprite;
            qCycleHub.cytcElectrons -= 1;
        }
        else if (cytochromeSprite.sprite == cytcRedSprite)
        {
            cytochromeBody.AddForce(forceDir * -forceMag, ForceMode2D.Force);
        }
    }
}
