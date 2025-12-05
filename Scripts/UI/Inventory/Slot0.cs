using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Slot0 : MonoBehaviour
{
    private InventoryManager manager;
    private Image image;
    private Image icon;
    private int slotIndex = 0;
    public Sprite palette1Sprite;
    public Sprite palette2Sprite;
    public Sprite palette3Sprite;

    private Color32 selectedColor = new Color32(140,140,140,255);
    private Color32 normalColor = new Color32(255,255,255,255);

    private float selectedPpu = 0.8f;
    private float normalPpu = 0.4f;

    private int lastPalette = -1;
    private int lastSelectedSlot = -1;

    void Start()
    {
        manager = FindAnyObjectByType<InventoryManager>();
        image = GetComponent<Image>();
        icon = transform.GetChild(0).GetComponent<Image>();
    }

    void Update()
    {
        // --- Update background only when selection changes ---
        if (manager.selectedSlot != lastSelectedSlot)
        {
            if (manager.selectedSlot == slotIndex)
            {
                image.color = selectedColor;
                image.pixelsPerUnitMultiplier = selectedPpu;
            }
            else
            {
                image.color = normalColor;
                image.pixelsPerUnitMultiplier = normalPpu;
            }

            lastSelectedSlot = manager.selectedSlot; // remember
        }

        // --- Update icon sprite only when palette changes ---
        if (manager.palette != lastPalette)
        {
            switch (manager.palette)
            {
                case 1: icon.sprite = palette1Sprite; break;
                case 2: icon.sprite = palette2Sprite; break;
                case 3: icon.sprite = palette3Sprite; break;
            }

            lastPalette = manager.palette;
        }
    }

    public void OnButtonPressed()
    {
        manager.selectedSlot = slotIndex;
    }
}