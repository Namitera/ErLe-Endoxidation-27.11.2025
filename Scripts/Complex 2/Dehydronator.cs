using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dehydronator : MonoBehaviour
{
    private SpriteRenderer fadBaseSprite;
    public Sprite fadh2Sprite;
    public Sprite fadSprite;
    public int craftableUbiquinones;

    void Awake()
    {
        craftableUbiquinones = 0;
    }

    void OnTriggerStay2D(Collider2D collision)
    {
        if (!collision.CompareTag("fadbase")) return;
        fadBaseSprite = collision.GetComponent<SpriteRenderer>();
        if (fadBaseSprite.sprite != fadh2Sprite) return;

        fadBaseSprite.sprite = fadSprite;
        craftableUbiquinones += 1;
    }
}
