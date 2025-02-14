document.addEventListener("DOMContentLoaded", function () {
    // Fetch data from your FastAPI backend
    fetch("http://127.0.0.1:8000/get-data")
      .then(response => response.json())
      .then(result => {
        console.log("Fetched result:", result);  // Debug: check your fetched data in the browser console
        // Ensure the response has the expected structure
        if (result.status === "success" && Array.isArray(result.data)) {
          const data = result.data;
          const table = document.getElementById("data-table");
          if (!table) {
            console.error("Table element with ID 'data-table' not found!");
            return;
          }
          const thead = table.querySelector("thead");
          const tbody = table.querySelector("tbody");
  
          // Clear existing content
          thead.innerHTML = "";
          tbody.innerHTML = "";
  
          // Generate table headers dynamically using keys from the first record
          const headers = Object.keys(data[0]);
          let headerRow = "<tr>";
          headers.forEach(key => {
            headerRow += `<th>${key}</th>`;
          });
          headerRow += "</tr>";
          thead.innerHTML = headerRow;
  
          // Generate table rows for each record
          let rowsHtml = "";
          data.forEach(item => {
            let row = "<tr>";
            headers.forEach(key => {
              // Safely display undefined or null values
              row += `<td>${item[key] !== undefined ? item[key] : ""}</td>`;
            });
            row += "</tr>";
            rowsHtml += row;
          });
          tbody.innerHTML = rowsHtml;
        } else {
          // If structure is unexpected or no data is present, show a fallback message
          document.querySelector("#data-table tbody").innerHTML =
            "<tr><td colspan='100%'>No data available.</td></tr>";
        }
      })
      .catch(error => console.error("Error fetching data:", error));
  });
  