using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Ship2Script : MonoBehaviour
{
    public Rigidbody rb;
    public Transform ship2;
    [Range(1.0f, 100.0f)]
    public float speed = 10.0f;
    public float alphaAng = 30.0f;
    public float betaDist = 100.0f;
    public Rigidbody ship2Rb;
    public GameObject ship2GO;
    public float errorRange = 3.0f;


    void Start()
    {
        rb = GetComponent<Rigidbody>();
        rb.velocity = new Vector3(0,0,speed);
        Random.InitState(0);
        StartCoroutine(Movement());
    }

    void Update()
    {
        //Get direction of ship2
        Vector3 targetDirection = ship2.position - transform.position;

        //Get angle of ship2
        float angle = Vector3.Angle(targetDirection, transform.forward);
 
        //get distance between ship1 and ship2
        float distance = Mathf.Abs(Vector3.Distance(ship2.position, transform.position));

        if (angle < alphaAng + errorRange && angle > alphaAng - errorRange){
            if(distance < betaDist + errorRange && distance > betaDist - errorRange){
                Destroy(ship2GO);
                rb.velocity = new Vector3(0,0,0);
                this.enabled = false;
                ship2.GetComponent<Ship1Script>().enabled = false;
            }
        }
        rb.velocity = transform.forward * speed;
    }
    private IEnumerator Movement()
    {
        while(true){
            yield return new WaitForSeconds(1);
            Defend(0.0f);
        }
    }
    public void Defend(float timeToWait){
        Quaternion targetRotation=Quaternion.LookRotation (new Vector3(0,0,0));
        var dist = Mathf.Abs(Vector3.Distance(ship2.position, transform.position));
        if(Mathf.Abs(dist) < 2000){
            Random.InitState(System.DateTime.Now.Millisecond);
            switch(Random.Range(0,3)){
            case 0:
                targetRotation = Quaternion.LookRotation (new Vector3(0,0,0));
                break;
            case 1:
                targetRotation = Quaternion.LookRotation (new Vector3(45,0,0));
                break;
            case 2:
                targetRotation = Quaternion.LookRotation (new Vector3(-45,0,0));
                break;
            case 3:
                targetRotation = Quaternion.LookRotation (ship2.position - transform.position + new Vector3(45,0,0));
                break;
            }
            // Debug.DrawRay(transform.position, targetRotation*Vector3.forward*10, Color.red);
            // Debug.Break();
            transform.rotation = Quaternion.Lerp(transform.rotation,targetRotation,Time.deltaTime*60);
        }
    }
}
