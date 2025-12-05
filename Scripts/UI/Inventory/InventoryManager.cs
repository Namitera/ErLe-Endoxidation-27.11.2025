using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class InventoryManager : MonoBehaviour
{
  public int palette;
  public bool canPlace;
  public int selectedSlot;
  private GameObject inventory;
  private LogicManagment manager;

    void Start()
    {
        manager = FindAnyObjectByType<LogicManagment>();
        inventory = GameObject.FindGameObjectWithTag("inventory");
        canPlace = false;
        selectedSlot = -1;
    }

    void Update()
    {
        if (manager.mode == 0)
        {
            inventory.SetActive(false);
        }
        if (manager.mode == 1)
        {
            if (inventory.activeSelf == false) inventory.SetActive(true);
        }
        palette = Mathf.Clamp(palette, 1, 3);

    }
}
