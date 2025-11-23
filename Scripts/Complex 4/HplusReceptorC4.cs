using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HplusReceptorC4 : MonoBehaviour
{
    public Oxidator oxidator;

    void Awake()
    {
        oxidator = GetComponentInParent<Oxidator>();
    }


    void OnTriggerEnter2D(Collider2D collision)
    {
        if (!collision.CompareTag("proton")) return;
        if (oxidator.usableProtons < oxidator.maxProtons)
        {
            oxidator.usableProtons += 1;
            Destroy(collision.gameObject);
        }
    }
}
