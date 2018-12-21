package com.hw.hw;

import android.Manifest;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import java.util.List;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = MainActivity.class.getSimpleName();
    TextView textview;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    /*--------------------------------------GPS module-----------------------------------------------*/
    /*---GPS initialization---*/
    LocationManager my_lm;
    String provider;

    //method when clicking the gps
    public void getlocation(View view)
    {
        List<String> list;

        textview = (TextView)findViewById(R.id.tv);

        // acquire available localization device
        list = my_lm.getProviders(true);
        if(list.contains(LocationManager.GPS_PROVIDER)){
            provider = LocationManager.GPS_PROVIDER;
            textview.append("GPS providing..."+"\n");
        }else
        {
            Toast.makeText(this, "PLease check whether the GPS is enabled", Toast.LENGTH_LONG).show();
        }

        if(ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)==PackageManager.PERMISSION_DENIED){
            return ;}
        if(ContextCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION)==PackageManager.PERMISSION_DENIED){
            return ;}

        String string;
        Location location = my_lm.getLastKnownLocation(provider);
        if(location!=null){
            string = "longitude: " + location.getLongitude() + "\n" + "latitude: " + location.getLatitude();
            Toast.makeText(this, string, Toast.LENGTH_SHORT).show();
        }
    }

    LocationListener my_ll = new LocationListener(){
        @Override
        public void onLocationChanged(Location location) {
            Log.d(TAG, "onlocationchanged: ");
            Log.d(TAG, "onlocationchanged: latitude = "+location.getLatitude());
            Log.d(TAG, "onlocationchanged: longitude = "+location.getLongitude());
            Log.d(TAG, "onlocationchanged: provider = "+location.getProvider());
            textview.append("longitude: "+location.getLongitude()+"\n"+"latitude: "+location.getLatitude());
        }
        @Override
        public void onStatusChanged(String provider, int status, Bundle extras){}
        @Override
        public void onProviderEnabled(String provider){}
        @Override
        public void onProviderDisabled(String provider){}
    };

    /*-------------------------------------Sensor module-----------------------------------------*/
    /* ---------------------- Sensor data ------------------- */
}
