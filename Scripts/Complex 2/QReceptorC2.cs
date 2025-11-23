using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QReceptorC2 : MonoBehaviour
{
    private Vector2 forceDir;
    private Rigidbody2D ubiquinoneBody;
    private SpriteRenderer ubiquinoneSprite;
    private Dehydronator dehydronator;
    public float forceMag = 10;
    public float reactionRadius = 3;
    public Sprite qSprite;
    public Sprite qh2Sprite;

    void Awake()
    {
        dehydronator = GetComponentInParent<Dehydronator>();        
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (!collision.CompareTag("ubiquinone")) return;

        ubiquinoneBody = collision.gameObject.GetComponent<Rigidbody2D>();
        ubiquinoneSprite = collision.gameObject.GetComponent<SpriteRenderer>();

        forceDir = (transform.position - ubiquinoneBody.transform.position).normalized;
        if (ubiquinoneSprite.sprite == qSprite)
        {
            if (dehydronator.craftableUbiquinones <= 0) return;
            ubiquinoneSprite.sprite = qh2Sprite;
            dehydronator.craftableUbiquinones -= 1;
        }
        else if (ubiquinoneSprite.sprite == qh2Sprite)
        {
            ubiquinoneBody.AddForce(forceDir * -forceMag, ForceMode2D.Force);
        }
    }
}