<template>
  <div>
    <AuthenticatedLayout>
      <div class="m-10">
        <div class="grid grid-cols-2 gap-4">
          <div class="bg-white p-4 rounded-lg">
            <h2 class="text-lg font-semibold mb-4">Line Chart</h2>
            <Chart
              :data="lineChartData"
              chartType="line"
              :chart-id="generateChartId()"
            />
          </div>

          <div class="bg-white p-4 rounded-lg">
            <h2 class="text-lg font-semibold mb-4">Bar Chart</h2>
            <Chart
              :data="barChartData"
              chartType="bar"
              :chart-id="generateChartId()"
            />
          </div>

          <div class="bg-white p-4 rounded-lg">
            <h2 class="text-lg font-semibold mb-4">Pie Chart</h2>
            <Chart
              :data="pieChartData"
              chartType="pie"
              :chart-id="generateChartId()"
            />
          </div>
        </div>
      </div>
    </AuthenticatedLayout>
  </div>
</template>

<script setup>
import AuthenticatedLayout from "../layouts/AuthenticatedLayout.vue";
import Chart from "../components/Chart.vue";

function generateChartId() {
  return `report-chart-${Date.now()}`; // Adjust ID generation as needed
}

// Sample data for Line Chart
const lineChartData = {
  labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
  datasets: [
    {
      label: "Sales",
      data: [30, 50, 100, 70, 60, 80],
      backgroundColor: "#3498db", // Blue color for the line
      borderColor: "#3498db", // Blue color for the line
    },
  ],
};

// Sample data for Bar Chart
const barChartData = {
  labels: ["Category A", "Category B", "Category C", "Category D"],
  datasets: [
    {
      label: "Sales",
      data: [200, 300, 400, 500],
      backgroundColor: ["#f39c12", "#e74c3c", "#9b59b6", "#2ecc71"], // Different colors for each bar
    },
  ],
};

// Sample data for Pie Chart
const pieChartData = {
  labels: ["Category A", "Category B", "Category C"],
  datasets: [
    {
      label: "Sales",
      data: [300, 200, 400],
      backgroundColor: ["#f39c12", "#e74c3c", "#9b59b6"], // Different colors for each segment
    },
  ],
};

const chartTypes = ["line", "bar", "pie"]; // Supported chart types
</script>
