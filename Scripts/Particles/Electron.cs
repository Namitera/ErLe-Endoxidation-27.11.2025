using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Electron : MonoBehaviour
{

    public Rigidbody2D body;
    public Vector2 randomDir;
    public SpriteRenderer protonBaseSprite;
    public Sprite hSprite;


    private float timerInit;
    private float timer;
    private CircleCollider2D trigger = null;
    private LogicManagment manager;


    void Start()
    {
        body = GetComponent<Rigidbody2D>();
        manager = FindFirstObjectByType<LogicManagment>();
        timerInit = Time.fixedTime;
        timer = 0;
    }
    void FixedUpdate()
    {
        randomDir = Random.insideUnitCircle;
        body.velocity += randomDir * manager.brownianMotionMultiplier;

        if (timer < 1)
        {
            if (timer > 0.5)
            {
                if (trigger != null) return;
                trigger = gameObject.AddComponent<CircleCollider2D>();
                trigger.isTrigger = true;
                trigger.radius = 0.51f;
            }
            timer = Time.fixedTime - timerInit;
        }
    }


    void OnTriggerEnter2D(Collider2D collision)
    {
        if (!collision.CompareTag("proton")) return;
        protonBaseSprite = collision.GetComponent<SpriteRenderer>();
        protonBaseSprite.sprite = hSprite;
        collision.tag = "hydrogen";
        Destroy(gameObject);
    } 
}
