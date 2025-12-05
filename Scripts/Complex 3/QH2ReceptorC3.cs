using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class QH2ReceptorC3 : MonoBehaviour
{
    private Vector2 forceDir;
    private Rigidbody2D ubiquinoneBody;
    private SpriteRenderer ubiquinoneSprite;
    private QCycleHub qCycleHub;
    public float forceMag = 10;
    public float reactionRadius = 3;
    public Sprite qSprite;
    public Sprite qh2Sprite;

    void Awake()
    {
        qCycleHub = GetComponentInParent<QCycleHub>();        
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (!collision.CompareTag("ubiquinone")) return;

        ubiquinoneBody = collision.gameObject.GetComponent<Rigidbody2D>();
        ubiquinoneSprite = collision.gameObject.GetComponent<SpriteRenderer>();

        forceDir = (transform.position - ubiquinoneBody.transform.position).normalized;
        if (ubiquinoneSprite.sprite == qh2Sprite)
        {
            ubiquinoneSprite.sprite = qSprite;
            qCycleHub.cytcElectrons += 1;
            qCycleHub.ubiquinoneElectrons += 1;
            qCycleHub.releasableProtons += 2;
        }
        else if (ubiquinoneSprite.sprite == qSprite)
        {
            ubiquinoneBody.AddForce(forceDir * -forceMag, ForceMode2D.Force);
        }
    }
}
