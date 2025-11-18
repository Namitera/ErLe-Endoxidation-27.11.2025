using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class ProtonPump : MonoBehaviour
{
    private Vector2 vecUp;
    private Vector2 forceDir;
    private Rigidbody2D protonBody;
    private Rigidbody2D particleBody;
    public float forceMag = 10;
    public int pumpableProtons;
    public int craftableUbiquinones;

    void Awake()
    {
        pumpableProtons = 0;
        craftableUbiquinones = 0;
    }

    void Update()
    {
        vecUp = transform.TransformDirection(Vector2.up);
        // Debug.Log(pumpableProtons);
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
