import React from "react";
import styles from "@/styles/Grid.module.css";

const gridData = [
  "House",
  "House",
  "House",
  "House",
  "House",
  "Street",
  "Street",
  "Street",
  "Street",
  "Street",
  "House",
  "House",
  "House",
  "Street",
  "House",
  "Street",
  "Street",
  "Street",
  "Street",
  "Street",
  "House",
  "House",
  "House",
  "Street",
  "House",
  "Street",
  "Street",
  "Street",
  "Street",
  "Street",
  "House",
  "House",
  "House",
  "Street",
  "House",
  "Street",
  "Street",
  "Street",
  "Street",
  "Street",
  "House",
  "House",
  "House",
  "Street",
  "House",
  "Street",
  "Street",
  "Street",
  "Street",
  "Street",
  "House",
  "House",
  "House",
  "Street",
  "House",
  "Street",
  "Street",
  "Street",
  "Street",
  "Street",
  "House",
  "House",
  "House",
  "Street",
  "House",
  "Street",
  "Street",
  "Street",
  "Street",
  "Street",
  "House",
  "House",
  "House",
  "Street",
  "House",
];

const GridContainer = () => {
  const rows = 15;
  const cols = 5;

  const getColorClass = (name) => {
    // Define different colors based on the name
    if (name === "House") {
      return styles.houseColor;
    } else if (name === "Street") {
      return styles.streetColor;
    }
    // Add more conditions for other names/colors as needed
    return "";
  };

  const renderGrid = () => {
    const gridItems = [];
    for (let i = 0; i < rows * cols; i++) {
      const nameIndex = i < gridData.length ? i : i % gridData.length;
      const name = gridData[nameIndex];
      const colorClass = getColorClass(name);

      gridItems.push(
        <div key={i} className={`${styles.gridItem} ${colorClass}`}>
          <span className={styles.gridItemText}>{name}</span>
        </div>
      );
    }
    return gridItems;
  };

  return <div className={styles.gridContainer}>{renderGrid()}</div>;
};

export default GridContainer;
