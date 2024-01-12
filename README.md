Deep link is a URL that takes users directly to specific content in an app. For example, the **example://myapp** deep link can be used to start **MainActivity**:
```
<activity android:name="MainActivity">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <!-- Accepts URIs that begin with "example://myapp -->
        <data android:scheme="example"
              android:host="myapp" />
    </intent-filter>
</activity>
```

This simple script will help you to collect the intent deep links from the both Manifest.xml(APK) & Plist(IPA). This will help you to start testing & discover Deep-link vulnerability.
