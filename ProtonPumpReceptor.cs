using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ProtonPumpReceptor : MonoBehaviour
{
    private Vector2 forceDir;
    private Rigidbody2D nadBody;
    private SpriteRenderer nadSprite;
    private ProtonPump protonPump;
    public float forceMag = 10;
    public float reactionRadius = 3;
    public Sprite nadhSprite;
    public Sprite nadplusSprite;

    void Awake()
    {
        protonPump = GetComponentInParent<ProtonPump>();        
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (!collision.CompareTag("nad")) return;

        nadBody = collision.gameObject.GetComponent<Rigidbody2D>();
        nadSprite = collision.gameObject.GetComponent<SpriteRenderer>();

        forceDir = (transform.position - nadBody.transform.position).normalized;
        if (nadSprite.sprite == nadhSprite)
        {
            // nadBody.AddForce(forceDir * forceMag, ForceMode2D.Force);
        }else if (nadSprite.sprite == nadplusSprite)
        {
            nadBody.AddForce(forceDir * -forceMag, ForceMode2D.Force);
        }


        // find if and clostest h
        if (Vector2.Distance(transform.position, nadBody.transform.position) < 3)
        {
            if (nadSprite.sprite != nadhSprite) return;

            Collider2D[] nearbyObj = Physics2D.OverlapCircleAll(transform.position, reactionRadius);

            float minDist = Mathf.Infinity;
            GameObject closestH = null;
            foreach (var candidate in nearbyObj)
            {
                if (!candidate.CompareTag("proton")) continue;
                float distance = Vector2.Distance(nadBody.transform.position, candidate.transform.position);

                if (distance > minDist) continue;
                minDist = distance;
                closestH = candidate.gameObject;
            }

            if (closestH != null)
            {
                Destroy(closestH);
                nadSprite.sprite = nadplusSprite;
                protonPump.pumpableProtons += 4;
            }
        }
    }
}
