using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;

public class AtpSynthase : MonoBehaviour
{
    public Vector2 vecUp;
    public Vector2 vecRight;
    public int pumpedProtons;
    public int craftableATP;
    [SerializeField]
    private float rotation;

    void Awake()
    {
        vecUp = transform.TransformDirection(Vector2.up);
        vecRight = transform.TransformDirection(Vector2.right);  
        pumpedProtons = 0;
        rotation = 0;
        craftableATP = 0;
    }


    void Update()
    {
        vecUp = transform.TransformDirection(Vector2.up);
        vecRight = transform.TransformDirection(Vector2.right);

        if (pumpedProtons > 0)
        {
            rotation += 0.125f * pumpedProtons;
            pumpedProtons = 0; 
        }

        if (rotation > 0.3333f)
        {
            rotation -= 0.3333f;
            craftableATP += 1;
        }
    }
}
