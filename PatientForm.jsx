import React, { useState } from "react";
import {
  TextField,
  Button,
  Select,
  MenuItem,
  InputLabel,
  FormControl,
  Container,
  Typography,
  Box,
} from "@mui/material";
import "./App.css";
import { green } from "@mui/material/colors";

const PatientForm = () => {
  // State to manage form inputs
  const [formData, setFormData] = useState({
    name: "",
    age: "",
    weight: "",
    sex: "",
    medications: "",
    allergies: "",
    alcoholUse: "",
    smoke: "",
  });

  // Function to handle text-to-speech
  const speak = (text) => {
    if ('speechSynthesis' in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      window.speechSynthesis.speak(utterance);
    } else {
      console.log("Text-to-speech is not supported in this browser.");
    }
  };

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submitted:", formData);
    // Add form submission logic (e.g., sending data to a server)
  };

  return (
    <Container maxWidth="sm" sx={{ display: "flex", justifyContent: "center" }}>
      <Box sx={{ mt: 4 }}>
        <Typography variant="h4" component="h2" gutterBottom>
          Patient Information Form
        </Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Name"
            variant="outlined"
            fullWidth
            margin="normal"
            name="name"
            value={formData.name}
            onChange={handleChange}
            onFocus={() => speak('Please enter your name')}
            required
          />

          <TextField
            label="Age"
            type="number"
            variant="outlined"
            fullWidth
            margin="normal"
            name="age"
            value={formData.age}
            onChange={handleChange}
            onFocus={() => speak('Please enter your age')}
            required
          />

          <TextField
            label="Weight (kg)"
            type="number"
            variant="outlined"
            fullWidth
            margin="normal"
            name="weight"
            value={formData.weight}
            onChange={handleChange}
            onFocus={() => speak('Please enter your weight')}
            required
          />

          <FormControl fullWidth margin="normal">
            <InputLabel>Sex</InputLabel>
            <Select
              label="Sex"
              name="sex"
              value={formData.sex}
              onChange={handleChange}
              onFocus={() => speak('Please select your sex')}
              required
            >
              <MenuItem value="">
                <em>Select</em>
              </MenuItem>
              <MenuItem value="male">Male</MenuItem>
              <MenuItem value="female">Female</MenuItem>
            </Select>
          </FormControl>

          <TextField
            label="Medications"
            variant="outlined"
            fullWidth
            margin="normal"
            name="medications"
            value={formData.medications}
            onChange={handleChange}
            onFocus={() => speak('Please list any medications you are taking')}
          />

          <TextField
            label="Allergies"
            variant="outlined"
            fullWidth
            margin="normal"
            name="allergies"
            value={formData.allergies}
            onChange={handleChange}
            onFocus={() => speak('Please list any allergies')}
          />

          <FormControl fullWidth margin="normal">
            <InputLabel>Do you drink alcohol?</InputLabel>
            <Select
              label="Do you drink alcohol?"
              name="alcoholUse"
              value={formData.alcoholUse}
              onChange={handleChange}
              onFocus={() => speak('Do you drink alcohol?')}
              required
            >
              <MenuItem value="">
                <em>Select</em>
              </MenuItem>
              <MenuItem value="Yes">Yes</MenuItem>
              <MenuItem value="No">No</MenuItem>
            </Select>
          </FormControl>

          <FormControl fullWidth margin="normal">
            <InputLabel>Do you smoke?</InputLabel>
            <Select
              label="Do you smoke?"
              name="smoke"
              value={formData.smoke}
              onChange={handleChange}
              onFocus={() => speak('Do you smoke?')}
              required
            >
              <MenuItem value="">
                <em>Select</em>
              </MenuItem>
              <MenuItem value="Yes">Yes</MenuItem>
              <MenuItem value="No">No</MenuItem>
            </Select>
          </FormControl>

          <Button
            type="submit"
            variant="contained"
            fullWidth
            sx={{ mt: 2 }}
            onFocus={() => speak('Submit the form')}
          >
            Submit
          </Button>
        </form>
      </Box>
    </Container>
  );
};

export default PatientForm;
