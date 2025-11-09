using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NAD : MonoBehaviour
{

    public Rigidbody2D body;
    public Vector2 randomDir;

    void Start()
    {
        body = GetComponent<Rigidbody2D>();
    }
    void FixedUpdate()
    {
        randomDir = Random.insideUnitCircle;
        body.velocity += randomDir;
    }
}
