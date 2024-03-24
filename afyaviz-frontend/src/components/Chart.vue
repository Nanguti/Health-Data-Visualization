<template>
  <canvas :id="chartId" class="h-full w-full"></canvas>
</template>

<script setup>
import { ref, onMounted } from "vue";
import {
  Chart as ChartJS,
  LineController,
  BarController,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  CategoryScale,
  BarElement,
  PieController,
  ArcElement,
} from "chart.js";

const props = defineProps({
  data: {
    type: Object,
    required: true,
  },
  chartType: {
    type: String,
    required: true,
  },
});

let chartIdCounter = 0;
function generateChartId() {
  return `chart-${props.chartType}-${chartIdCounter++}`;
}

const chartId = ref(generateChartId());

// const chartId = ref("myChart");
let dynamicChart = null;
const options = {
  scales: {
    y: {
      ticks: {
        beginAtZero: true,
      },
    },
  },
};

onMounted(() => {
  const ctx = document.getElementById(chartId.value).getContext("2d");
  ChartJS.register(
    LineController,
    PieController,
    BarController,
    BarElement,
    LineElement,
    PointElement,
    LinearScale,
    ArcElement,
    Title,
    CategoryScale
  );

  // Check if dynamicChart exists and destroy it if it does
  if (dynamicChart) {
    dynamicChart.destroy();
  }

  dynamicChart = new ChartJS(ctx, {
    type: props.chartType, // Use the chart type passed as a prop
    data: props.data,
    options: options,
  });
});
</script>
