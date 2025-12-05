using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using UnityEngine.UI;

public class SpawnButton : MonoBehaviour
{
    private LogicManagment manager;
    public Sprite particle;
    public Sprite nad;
    public Sprite fad;
    public Sprite electron;
    public Sprite ubiquinone;
    public Sprite cytochromec;
    public Sprite oxygen;
    public Sprite adp;
    public Sprite phosphorus;
    private Image image;
    private Sprite targetSprite;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
        image = GetComponent<Image>();
        targetSprite = particle;
    }

    public void OnButtonPressed()
    {
        manager.spawnButtonPressed = true;
    }

    void Update()
    {
        targetSprite = manager.toSpawnParticle.GetComponent<SpriteRenderer>().sprite;
        image.sprite = targetSprite;
    }
}
