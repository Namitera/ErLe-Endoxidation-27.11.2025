using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Oxygen : MonoBehaviour
{

    public Rigidbody2D body;
    public Vector2 randomDir;
    private LogicManagment manager;

    void Start()
    {
        body = GetComponent<Rigidbody2D>();
        manager = FindFirstObjectByType<LogicManagment>();
    }
    void FixedUpdate()
    {
        randomDir = Random.insideUnitCircle;
        body.velocity += randomDir * manager.brownianMotionMultiplier;
    }
}
