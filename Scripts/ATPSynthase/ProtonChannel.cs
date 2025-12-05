using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ProtonChannel : MonoBehaviour
{
    private AtpSynthase atpSynthase;
    private Vector3 vecUp;
    private Vector3 vecRight;

    private Vector2 forceDir;
    private Rigidbody2D protonBody;
    private Rigidbody2D particleBody;
    public float forceMag = 10;

    void Awake()
    {
        atpSynthase = GetComponentInParent<AtpSynthase>();

        vecUp = new Vector3(atpSynthase.vecUp.x, atpSynthase.vecUp.y, 0);
        vecRight = new Vector3(atpSynthase.vecRight.x, atpSynthase.vecRight.y, 0);
    }

    void Update()
    {
        vecUp = new Vector3(atpSynthase.vecUp.x, atpSynthase.vecUp.y, 0);
        vecRight = new Vector3(atpSynthase.vecRight.x, atpSynthase.vecRight.y, 0);
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (collision.attachedRigidbody != null)
        {
            if (!collision.CompareTag("protonk1"))
            {
                particleBody = collision.gameObject.GetComponent<Rigidbody2D>();
                forceDir = (transform.position - particleBody.transform.position).normalized;
                particleBody.AddForce(-forceDir * forceMag, ForceMode2D.Force);
            }
            
            if (collision.CompareTag("proton") && Vector2.Dot(forceDir, vecRight) > 0)
            {
                collision.tag = "protonk1";
            }
        }

        if (!collision.CompareTag("protonk1")) return;
        protonBody = collision.gameObject.GetComponent<Rigidbody2D>();

        forceDir = (transform.position - protonBody.transform.position).normalized;
        if (Vector2.Dot(forceDir, vecRight) < 0){ collision.tag = "proton"; atpSynthase.pumpedProtons += 1; }
        protonBody.AddForce(forceDir * forceMag, ForceMode2D.Force);     
    }
}
