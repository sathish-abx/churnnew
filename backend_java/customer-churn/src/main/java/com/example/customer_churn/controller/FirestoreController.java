package com.example.customer_churn.controller;

import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.QueryDocumentSnapshot;
import com.google.firebase.cloud.FirestoreClient;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ExecutionException;
import java.util.stream.Collectors;

@RestController
public class FirestoreController {

    @GetMapping("/data/{collectionName}")
    public ResponseEntity<?> getData(@PathVariable String collectionName) {
        // Check if collectionName is provided
        if (collectionName == null || collectionName.isEmpty()) {
            return ResponseEntity.badRequest().body("collectionName parameter is required");
        }

        try {
            // Fetch data from Firestore
            Firestore db = FirestoreClient.getFirestore();
            List<QueryDocumentSnapshot> documents = db.collection(collectionName).get().get().getDocuments();

            // Convert QueryDocumentSnapshot to Map
            List<Map<String, Object>> result = documents.stream()
                    .map(document -> {
                        Map<String, Object> data = new HashMap<>();
                        data.put("id", document.getId()); // Include document ID
                        data.putAll(document.getData());  // Include document fields
                        return data;
                    })
                    .collect(Collectors.toList());

            // Return the data as JSON
            return ResponseEntity.ok(result);
        } catch (ExecutionException | InterruptedException e) {
            // Handle Firestore errors
            return ResponseEntity.internalServerError().body("Error fetching data from Firestore: " + e.getMessage());
        }
    }
}