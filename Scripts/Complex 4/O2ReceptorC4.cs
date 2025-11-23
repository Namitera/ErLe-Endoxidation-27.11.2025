using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class O2ReceptorC4 : MonoBehaviour
{
    private Vector2 forceDir;
    public GameObject oxygen;
    private Rigidbody2D oxygenBody;
    private SpriteRenderer oxygenBaseSprite;
    private Oxidator oxidator;
    public float forceMag = 10;
    public float reactionRadius = 3;
    public Sprite oxygenSprite;
    public Sprite waterSprite;

    void Awake()
    {
        oxidator = GetComponentInParent<Oxidator>();        
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (!collision.CompareTag("oxygen")) return;

        oxygenBody = collision.gameObject.GetComponent<Rigidbody2D>();
        oxygenBaseSprite = collision.gameObject.GetComponent<SpriteRenderer>();

        forceDir = (transform.position - oxygenBody.transform.position).normalized;
        if (oxygenBaseSprite.sprite == oxygenSprite)
        {
            if (oxidator.usableProtons < 4 || oxidator.oxygenElectrons < 4) return;
            oxygenBaseSprite.sprite = waterSprite;
            oxygenBody.tag = "water";

            GameObject newWater = Instantiate(oxygen, transform.position, Quaternion.identity);
            SpriteRenderer renderer = newWater.GetComponent<SpriteRenderer>();
            renderer.sprite = waterSprite;
            newWater.tag = "water";

            oxidator.oxygenElectrons -= 4;
            oxidator.usableProtons -= 4;
            oxidator.pumpableProtons += 4;
        }
        else if (oxygenBaseSprite.sprite == waterSprite)
        {
            oxygenBody.AddForce(forceDir * -forceMag, ForceMode2D.Force);
        }
    }
}
