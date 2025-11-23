using System;
using System.Collections.Generic;
using System.Linq;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.WSA;

public class Trash : MonoBehaviour
{
    public float frequency = 1;
    public int amount = 1;
    public float radius = 1;
    public GameObject destroyObject;
    public Sprite destroySprite;
    private Type destroyType;
    private SpriteRenderer destroyRenderer;
    private CircleCollider2D trigger;
    private List<GameObject> inside = new List<GameObject>();
    private float time;
    private bool canTrash;

    void Awake()
    {
        canTrash = false;
        trigger = gameObject.AddComponent<CircleCollider2D>();
        trigger.isTrigger = true;
        destroyType = destroyObject.GetComponent<MonoBehaviour>().GetType();

        destroyRenderer = destroyObject.GetComponent<SpriteRenderer>();
        if (destroySprite == null) destroySprite = destroyRenderer.sprite;
    }

    void FixedUpdate()
    {
        time = Time.fixedTime;
        this.name = "Trash" + " (" + destroyObject.name + ")";

        trigger.radius = radius;

        if (canTrash && time % frequency < (0.5 * frequency))
        {
            canTrash = false;
            if (destroyObject == null) return;
            int deleted = 0;
            foreach (var obj in inside.ToArray())
            {
                if (obj.GetComponent(destroyType) != null && destroySprite == obj.GetComponent<SpriteRenderer>().sprite)
                {
                    inside.Remove(obj);
                    Destroy(obj);
                    deleted ++;
                    if (deleted >= amount) break;
                }
            }
        }

        if (time % frequency > (0.5 * frequency))
        {
            canTrash = true;
        }
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (!inside.Contains(collision.gameObject))
        {
            inside.Add(collision.gameObject);
        }        
    }

    void OnTriggerExit2D(Collider2D collision)
    {
    {
        if (inside.Contains(collision.gameObject))
        {
            inside.Remove(collision.gameObject);
        }
    }
    }
}
