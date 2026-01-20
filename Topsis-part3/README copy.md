# TOPSIS Web Application

A web application implementing the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) algorithm for multi-criteria decision analysis.

## Features

- Upload CSV or Excel (.xlsx) files containing decision matrices
- Automated computation of TOPSIS scores and rankings
- Interactive preview of results in the browser
- Email delivery of analysis results
- Download results in CSV format
- Comprehensive input validation for weights, impacts, and email
- Responsive, modern user interface
- Easy deployment to Vercel

## Setup Instructions

### 1. EmailJS Configuration

To enable the email functionality, configure EmailJS as follows:

1. Visit [EmailJS](https://www.emailjs.com/) and create a free account
2. Add an email service (such as Gmail or Outlook)
3. Create an email template with the following variables:
   - `{{to_email}}` - Recipient's email address
   - `{{file_name}}` - Original filename
   - `{{results}}` - TOPSIS results preview

4. Obtain your credentials:
   - **Public Key**: Located in Account > API Keys
   - **Service ID**: Found in Email Services
   - **Template ID**: Found in Email Templates

5. Update `app.js` with your credentials:
   ```javascript
   // Line 4: Replace YOUR_PUBLIC_KEY
   emailjs.init('YOUR_PUBLIC_KEY');
   
   // Line 284: Replace YOUR_SERVICE_ID and YOUR_TEMPLATE_ID
   await emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams);
   ```

### 2. Local Testing

To test the application locally:

1. Open `index.html` directly in a web browser
2. Alternatively, use a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   ```

### 3. Deploy to Vercel

To deploy the application on Vercel:

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Navigate to the project directory:
   ```bash
   cd Topsis-Part3
   ```

3. Deploy the application:
   ```bash
   vercel
   ```

4. Follow the on-screen prompts to complete the deployment

## How to Use

1. **Upload File**: Select a CSV or XLSX file
   - The first column should contain identifiers (names, IDs, etc.)
   - Subsequent columns should contain numeric criteria values

2. **Enter Weights**: Provide comma-separated numeric values
   - Example: `1,1,1,2`
   - The number must match the number of criteria columns

3. **Enter Impacts**: Provide comma-separated `+` or `-` symbols
   - `+` for beneficial criteria (higher values are better)
   - `-` for non-beneficial criteria (lower values are better)
   - Example: `+,+,-,+`

4. **Enter Email**: Provide a valid email address to receive the results

5. **Submit**: Click "Analyze & Send Results"

6. **View Results**: Preview the results in the browser and check your email

7. **Download**: Click "Download Results" to save the CSV file

## Input File Format

### Example CSV:
```csv
Model,Price,Storage,Camera,Looks
M1,250,16,12,5
M2,200,16,8,3
M3,300,32,16,4
M4,275,32,8,4
M5,225,16,16,2
```

### Requirements:
- At least 3 columns (1 identifier + 2+ criteria)
- All criteria columns must contain numeric values
- First row contains headers
- CSV or XLSX format

## Validation Rules

- Number of weights = Number of impacts = Number of criteria
- Weights must be numeric values
- Impacts must be either `+` or `-`
- All separated by commas
- Valid email format
- All criteria values must be numeric

## Technologies Used

- **HTML5** - Structure
- **CSS3** - Styling with modern gradients and animations
- **JavaScript (ES6+)** - TOPSIS algorithm implementation
- **XLSX.js** - Excel file parsing
- **EmailJS** - Email delivery service
- **Vercel** - Hosting platform

## File Structure

```
Topsis-Part3/
├── index.html          # Main HTML page
├── styles.css          # Styling and animations
├── app.js              # TOPSIS algorithm and email functionality
├── sample-data.csv     # Sample input data
├── vercel.json         # Vercel deployment configuration
└── README copy.md      # Documentation
```

## TOPSIS Algorithm Overview

1. **Normalization**: Normalize the decision matrix using vector normalization
2. **Weighted Matrix**: Multiply normalized values by their respective weights
3. **Ideal Solutions**: Determine the ideal best and worst solutions
4. **Distance Calculation**: Compute Euclidean distances from ideal solutions
5. **TOPSIS Score**: Calculate relative closeness to the ideal solution
6. **Ranking**: Rank alternatives based on their TOPSIS scores

## Troubleshooting

### Email Not Sending
- Verify EmailJS credentials are correct
- Check EmailJS dashboard for error logs
- Ensure email service is active
- Check browser console for errors

### File Upload Issues
- Ensure file is in CSV or XLSX format
- Check that all criteria values are numeric
- Verify file has at least 3 columns

### Validation Errors
- Count the number of commas in weights/impacts
- Ensure impacts only use `+` or `-` characters
- Match weights/impacts count to number of criteria columns

## License

MIT License - Free to use and modify

## Support

For any issues or questions, please create an issue in the repository.
