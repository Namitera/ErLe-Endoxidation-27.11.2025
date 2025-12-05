using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlaceButton : MonoBehaviour
{
   private InventoryManager manager;

    void Start()
    {
        manager = FindAnyObjectByType<InventoryManager>();
    }

    public void OnButtonPressed()
    {
        manager.canPlace = true;
    }
}
