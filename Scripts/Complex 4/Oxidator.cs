using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Oxidator : MonoBehaviour
{
    private Vector2 vecUp;
    private Vector2 forceDir;
    private Rigidbody2D protonBody;
    private Rigidbody2D particleBody;

    public float forceMag = 10;
    public int oxygenElectrons;
    public int usableProtons;
    public int maxProtons;
    public int pumpableProtons;


    void Awake()
    {
        oxygenElectrons = 0;
        usableProtons = 0;
        maxProtons = 4;
        pumpableProtons = 0;
    }

    void Update()
    {
        vecUp = transform.TransformDirection(Vector2.up);
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
            
            if (collision.CompareTag("proton") && pumpableProtons > 0 && Vector2.Dot(forceDir, vecUp) > 0)
            {
                collision.tag = "protonk1"; pumpableProtons -= 1;
            }
        }

        if (!collision.CompareTag("protonk1")) return;
        protonBody = collision.gameObject.GetComponent<Rigidbody2D>();

        forceDir = (transform.position - protonBody.transform.position).normalized;
        if (Vector2.Dot(forceDir, vecUp) < 0) collision.tag = "proton";
        protonBody.AddForce(forceDir * forceMag, ForceMode2D.Force);     
    }
}
