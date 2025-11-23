using System.Collections;
using System.Collections.Generic;
using Unity.Mathematics;
using UnityEngine;

public class Shaft : MonoBehaviour
{
    private AtpSynthase atpSynthase;
    private float toRotate;
    private float oldRotation;
    public float speed = 0.1f;

    void Awake()
    {
        atpSynthase = GetComponentInParent<AtpSynthase>();
        toRotate = 0;
        oldRotation = 0;
    }

    void Update()
    {
        if (atpSynthase.totalRotation > oldRotation)
        {
            toRotate += 360 * (atpSynthase.totalRotation - oldRotation);
            oldRotation = atpSynthase.totalRotation;
        }

        transform.rotation *= Quaternion.Euler(0, toRotate*speed, 0);
        toRotate *= 1 - speed;
    }
}
