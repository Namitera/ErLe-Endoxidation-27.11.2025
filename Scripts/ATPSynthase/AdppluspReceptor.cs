using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AdppluspReceptor : MonoBehaviour
{
    private AtpSynthase atpSynthase;
    public int storedPhosphorus;
    public int storedAdp;
    private Vector3 vecUp;
    private Vector3 vecRight;
    public Sprite atpSprite;


    void Awake()
    {
        atpSynthase = GetComponentInParent<AtpSynthase>();
        storedPhosphorus = 0;
        storedAdp = 0;

        vecUp = new Vector3(atpSynthase.vecUp.x, atpSynthase.vecUp.y, 0);
        vecRight = new Vector3(atpSynthase.vecRight.x, atpSynthase.vecRight.y, 0);
    }

    void Update()
    {
        vecUp = new Vector3(atpSynthase.vecUp.x, atpSynthase.vecUp.y, 0);
        vecRight = new Vector3(atpSynthase.vecRight.x, atpSynthase.vecRight.y, 0);

        if (atpSynthase.craftableATP > 0 && storedAdp > 0 && storedPhosphorus > 0)
        {
            atpSynthase.craftableATP -= 1;
            storedPhosphorus -= 1;
            storedAdp -=1;
            Destroy(GameObject.FindGameObjectWithTag("phosphorusk5"));
            GameObject toConvertAdp = GameObject.FindGameObjectWithTag("adpk5");
            SpriteRenderer renderer = toConvertAdp.GetComponent<SpriteRenderer>();
            renderer.sprite = atpSprite;
            toConvertAdp.tag = "atp";
            toConvertAdp.transform.position = transform.position + vecRight*5;
        }
    }

    void OnTriggerEnter2D(Collider2D collision)
    {
        if (!collision.CompareTag("phosphorus") && !collision.CompareTag("adp")) return;
        
        if (collision.CompareTag("phosphorus") && storedPhosphorus < 3)
        {
            collision.transform.position = transform.position - vecRight*4 + vecUp*5;
            storedPhosphorus += 1;
            collision.tag = "phosphorusk5";
        }

        if (collision.CompareTag("adp") && storedAdp < 3)
        {
            collision.transform.position = transform.position - vecRight*4 - vecUp*5;
            storedAdp += 1;
            collision.tag = "adpk5";
        }
    }
}
