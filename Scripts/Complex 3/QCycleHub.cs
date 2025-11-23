using System.Collections;
using System.Collections.Generic;
using Unity.Mathematics;
using UnityEngine;

public class QCycleHub : MonoBehaviour
{
    private Vector2 vecUp;
    public GameObject proton;

    public int cytcElectrons;
    public int ubiquinoneElectrons;
    public int releasableProtons;
    public int usableProtons;


    void Awake()
    {
        cytcElectrons = 0;
        ubiquinoneElectrons = 0;
        releasableProtons = 0;
        usableProtons = 0;
    }

    void Update()
    {
        vecUp = transform.TransformDirection(Vector2.up); 

        if (releasableProtons > 0)
        {
            Vector3 offset = 15 * new Vector3(vecUp.x, vecUp.y, 0);
            Instantiate(proton, transform.position + offset, Quaternion.identity);
            releasableProtons -= 1;
        }
    }


    void OnTriggerEnter2D(Collider2D collision)
    {
        if (!collision.CompareTag("proton")) return;
        if (usableProtons < ubiquinoneElectrons)
        {
            usableProtons += 1;
            Destroy(collision.gameObject);
        }
    }
}
