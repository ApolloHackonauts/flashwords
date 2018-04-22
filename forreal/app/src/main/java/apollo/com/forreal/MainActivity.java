package apollo.com.forreal;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.android.volley.AuthFailureError;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.gson.Gson;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {
    ImageView imageView;
    ArrayList<FlashCard> cards;
    int current_idx;
    boolean answer_shown;
    String answered, unanswered;
    ImageButton next_button;
    ImageButton prev_button;
    ImageButton speak_button;
    ImageButton cam_button;
    Button answer_button;
    TextView textView;
    Bitmap last_image;
    String goog_url = "http://127.0.0.1:5000";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        next_button = (ImageButton) findViewById(R.id.next_button);
        next_button.setVisibility(View.INVISIBLE);
        prev_button = (ImageButton) findViewById(R.id.prev_button);
        prev_button.setVisibility(View.INVISIBLE);
        speak_button = (ImageButton) findViewById(R.id.speak_button);
        speak_button.setVisibility(View.INVISIBLE);
        cam_button = (ImageButton) findViewById(R.id.cam_button);
        answer_button = (Button) findViewById(R.id.answer_button);
        answer_button.setVisibility(View.INVISIBLE);
        textView = (TextView) findViewById(R.id.textView);
        textView.setVisibility(View.INVISIBLE);
        imageView = (ImageView)findViewById(R.id.imageView);
        cards = new ArrayList<FlashCard>();
        answer_shown = false;
        answered = "Show original";
        unanswered = "Show translation";

        answer_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v){
                if (answer_shown){
                    textView.setText(cards.get(current_idx).native_word);
                }else {
                    textView.setText(cards.get(current_idx).translated_word);
                }
                answer_shown = !answer_shown; //toggle
                updateAnswerButton();
            }
        });
        next_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (current_idx > 0){
                    ++current_idx;
                }
                imageView.setImageBitmap(cards.get(current_idx).object_image);
                answer_shown = false;
                textView.setText(cards.get(current_idx).native_word);
                updateAnswerButton();
            }
        });

        prev_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                if (current_idx < cards.size() - 1){
                    --current_idx;
                }
                imageView.setImageBitmap(cards.get(current_idx).object_image);
                answer_shown = false;
                textView.setText(cards.get(current_idx).native_word);
                updateAnswerButton();
            }
        });

        cam_button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(intent,0);
            }
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data){
        super.onActivityResult(requestCode,resultCode,data);
        if (resultCode == RESULT_OK) {
            last_image = (Bitmap) data.getExtras().get("data");
            ArrayList<FlashCard> stub = new ArrayList<FlashCard>();
            FlashCard stubcard = new FlashCard();
            stubcard.native_word = "native";
            stubcard.translated_word = "trans";
            stubcard.object_image = last_image;
            stub.add(stubcard);
            addCards(stub);
            //addCards(makeCards(response));//TODO uncomm this
        }
    }

    protected void addCards(ArrayList<FlashCard> cards){
        if (this.cards.size() == 0 && cards.size() > 0) {
            this.current_idx = 0;
            next_button.setVisibility(View.VISIBLE);
            prev_button.setVisibility(View.VISIBLE);
            textView.setText(unanswered);
            textView.setVisibility(View.VISIBLE);
            answer_button.setVisibility(View.VISIBLE);
            this.cards.addAll(cards);
            textView.setText(this.cards.get(current_idx).native_word);
            imageView.setImageBitmap(this.cards.get(current_idx).object_image);
        }
    }

    protected void updateAnswerButton(){
        if (answer_shown){
            answer_button.setText(answered);
        }else{
            answer_button.setText(unanswered);
        }
    }

    protected Bitmap cropImage(Bitmap bitmap, int x1, int y1, int x2, int y2){
        int width = Math.abs(x1-x2);
        int height = Math.abs(y1-y2);
        return Bitmap.createBitmap(bitmap,x1,y1,width, height);
    }

    protected ArrayList<FlashCard> makeCards(String bytes){
        final ArrayList<FlashCard> cards = new ArrayList<FlashCard>();



        try {
            JSONObject jsonBody = new JSONObject();
            jsonBody.put("filename", bytes);
            jsonBody.put("filetype", "jpg");
            jsonBody.put("translated_lang", "spanish");
            final String requestBody = jsonBody.toString();

            StringRequest stringRequest = new StringRequest(1, goog_url, new Response.Listener<String>() {
                @Override
                public void onResponse(JSONObject response) {
                    JSONArray j = response.optJSONArray("results");
                    //loop through response adding FlashCards to cards
                    for (int i = 0; i < j.length(); ++i){
                        FlashCard f = new FlashCard();
                        Gson g = new Gson();

                        f.translated_word = "";
                        f.object_image = cropImage(last_image,0,0,0, 0);
                        cards.add(f);
                    }
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {

                }
            }) {
                @Override
                public String getBodyContentType() {
                    return String.format("application/json; charset=utf-8");
                }

                @Override
                public byte[] getBody() throws AuthFailureError{
                    try {
                        return requestBody == null ? null : requestBody.getBytes("utf-8";
                    } catch (UnsupportedEncodingException uee) {
                        VolleyLog.wtf("Unsupported Encoding while trying to get the bytes of %s using %s",
                                requestBody, "utf-8");
                        return null;
                    }
                }
            };

            RequestQueue requestQueue = Volley.newRequestQueue(this);
            requestQueue.add(stringRequest);
        } catch (JSONException e) {
            e.printStackTrace();
        }

        return cards;
    }
}
