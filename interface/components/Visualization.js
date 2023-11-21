import React, { useState, useEffect } from "react";
import Graph from "react-graph-vis";

let djson = [
  {
    "Buyer": "Buyer2C",
    "Seller": "Seller20A",
    "Quantity": 140,
    "Price": 11.5
  },
  {
    "Buyer": "Buyer2A",
    "Seller": "Seller20A",
    "Quantity": 110,
    "Price": 11
  },
  {
    "Buyer": "Buyer2A",
    "Seller": "Seller19A",
    "Quantity": 40,
    "Price": 11
  },
  {
    "Buyer": "Buyer1C",
    "Seller": "Seller19A",
    "Quantity": 90,
    "Price": 10.5
  },
  {
    "Buyer": "Buyer2B",
    "Seller": "Seller19A",
    "Quantity": 110,
    "Price": 10.5
  },
  {
    "Buyer": "Buyer2B",
    "Seller": "Seller20B",
    "Quantity": 50,
    "Price": 10.5
  },
  {
    "Buyer": "Buyer3C",
    "Seller": "Seller20B",
    "Quantity": 190,
    "Price": 10.3
  },
  {
    "Buyer": "Buyer3A",
    "Seller": "Seller20B",
    "Quantity": 5,
    "Price": 10.2
  },
  {
    "Buyer": "Buyer3A",
    "Seller": "Seller18A",
    "Quantity": 195,
    "Price": 10.2
  },
  {
    "Buyer": "Buyer1A",
    "Seller": "Seller18A",
    "Quantity": 35,
    "Price": 10
  },
  {
    "Buyer": "Buyer1A",
    "Seller": "Seller19B",
    "Quantity": 65,
    "Price": 10
  },
  {
    "Buyer": "Buyer3B",
    "Seller": "Seller19B",
    "Quantity": 170,
    "Price": 10
  },
  {
    "Buyer": "Buyer3B",
    "Seller": "Seller20C",
    "Quantity": 10,
    "Price": 10
  },
  {
    "Buyer": "Buyer1B",
    "Seller": "Seller20C",
    "Quantity": 120,
    "Price": 9.5
  },
  {
    "Buyer": "Buyer4B",
    "Seller": "Seller20C",
    "Quantity": 110,
    "Price": 9.3
  },
  {
    "Buyer": "Buyer4C",
    "Seller": "Seller17A",
    "Quantity": 105,
    "Price": 9.1
  },
  {
    "Buyer": "Buyer4A",
    "Seller": "Seller17A",
    "Quantity": 100,
    "Price": 9
  },
  {
    "Buyer": "Buyer5C",
    "Seller": "Seller17A",
    "Quantity": 15,
    "Price": 8.9
  },
  {
    "Buyer": "Buyer5C",
    "Seller": "Seller18B",
    "Quantity": 215,
    "Price": 8.9
  },
  {
    "Buyer": "Buyer5B",
    "Seller": "Seller18B",
    "Quantity": 10,
    "Price": 8.7
  },
  {
    "Buyer": "Buyer5B",
    "Seller": "Seller19C",
    "Quantity": 230,
    "Price": 8.7
  },
  {
    "Buyer": "Buyer6C",
    "Seller": "Seller16A",
    "Quantity": 210,
    "Price": 8.7
  },
  {
    "Buyer": "Buyer6C",
    "Seller": "Seller17B",
    "Quantity": 30,
    "Price": 8.7
  },
  {
    "Buyer": "Buyer5A",
    "Seller": "Seller17B",
    "Quantity": 185,
    "Price": 8.5
  },
  {
    "Buyer": "Buyer5A",
    "Seller": "Seller18C",
    "Quantity": 65,
    "Price": 8.5
  },
  {
    "Buyer": "Buyer6B",
    "Seller": "Seller18C",
    "Quantity": 155,
    "Price": 8.5
  },
  {
    "Buyer": "Buyer6B",
    "Seller": "Seller15A",
    "Quantity": 95,
    "Price": 8.5
  },
  {
    "Buyer": "Buyer7C",
    "Seller": "Seller15A",
    "Quantity": 105,
    "Price": 8.5
  },
  {
    "Buyer": "Buyer7C",
    "Seller": "Seller16B",
    "Quantity": 145,
    "Price": 8.5
  },
  {
    "Buyer": "Buyer6A",
    "Seller": "Seller16B",
    "Quantity": 60,
    "Price": 8.3
  },
  {
    "Buyer": "Buyer6A",
    "Seller": "Seller17C",
    "Quantity": 200,
    "Price": 8.3
  },
  {
    "Buyer": "Buyer7B",
    "Seller": "Seller17C",
    "Quantity": 10,
    "Price": 8.3
  },
  {
    "Buyer": "Buyer7B",
    "Seller": "Seller14A",
    "Quantity": 190,
    "Price": 8.3
  },
  {
    "Buyer": "Buyer7B",
    "Seller": "Seller15B",
    "Quantity": 60,
    "Price": 8.3
  },
  {
    "Buyer": "Buyer8C",
    "Seller": "Seller15B",
    "Quantity": 135,
    "Price": 8.3
  },
  {
    "Buyer": "Buyer8C",
    "Seller": "Seller16C",
    "Quantity": 125,
    "Price": 8.3
  },
  {
    "Buyer": "Buyer7A",
    "Seller": "Seller16C",
    "Quantity": 75,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer7A",
    "Seller": "Seller13A",
    "Quantity": 180,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer7A",
    "Seller": "Seller14B",
    "Quantity": 15,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer8B",
    "Seller": "Seller14B",
    "Quantity": 170,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer8B",
    "Seller": "Seller15C",
    "Quantity": 100,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer9C",
    "Seller": "Seller15C",
    "Quantity": 90,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer9C",
    "Seller": "Seller12A",
    "Quantity": 170,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer9C",
    "Seller": "Seller13B",
    "Quantity": 10,
    "Price": 8.1
  },
  {
    "Buyer": "Buyer8A",
    "Seller": "Seller13B",
    "Quantity": 165,
    "Price": 7.9
  },
  {
    "Buyer": "Buyer8A",
    "Seller": "Seller14C",
    "Quantity": 115,
    "Price": 7.9
  },
  {
    "Buyer": "Buyer9B",
    "Seller": "Seller14C",
    "Quantity": 65,
    "Price": 7.9
  },
  {
    "Buyer": "Buyer9B",
    "Seller": "Seller11A",
    "Quantity": 160,
    "Price": 7.9
  },
  {
    "Buyer": "Buyer9B",
    "Seller": "Seller12B",
    "Quantity": 55,
    "Price": 7.9
  },
  {
    "Buyer": "Buyer10C",
    "Seller": "Seller12B",
    "Quantity": 110,
    "Price": 7.9
  },
  {
    "Buyer": "Buyer10C",
    "Seller": "Seller13C",
    "Quantity": 170,
    "Price": 7.9
  }
 ]

const options = {
  layout: {
    hierarchical: false,
  },
  edges: {
    color: "#008000",
  },
  physics: {
    enabled: false,
  },
};

const generateUniqueID = () => {
  return '_' + Math.random().toString(36).substr(2, 9);
};

export default function Visualization() {
  const [state, setState] = useState({
    graph: {
      nodes: [],
      edges: [],
    },
    events: {
      // Event handlers...
    },
  });
  const [currentEdgeIndex, setCurrentEdgeIndex] = useState(1);

  const randomSort = () => Math.random() - 0.5;

  djson = djson.sort(randomSort);

  useEffect(() => {
    const buyersSet = new Set();
    const sellersSet = new Set();
  
    djson.forEach((sale) => {
      buyersSet.add(sale.Buyer);
      sellersSet.add(sale.Seller);
    });
  
    const sellerNodes = Array.from(sellersSet).map((seller, index) => ({
      id: `seller_${index}`,
      label: `${seller}`,
      x: -200,
      y: index * 50,
    }));
  
    const buyerNodes = Array.from(buyersSet).map((buyer, index) => ({
      id: `buyer_${index}`,
      label: `${buyer}`,
      x: 200,
      y: index * 50,
    }));
  
    setState((prevState) => ({
      ...prevState,
      graph: {
        nodes: [...sellerNodes, ...buyerNodes],
        edges: prevState.graph.edges,
      },
    }));
  
    const salesEdges = djson.map((sale) => ({
      from: `seller_${Array.from(sellersSet).indexOf(sale.Seller)}`,
      to: `buyer_${Array.from(buyersSet).indexOf(sale.Buyer)}`,
      label: `Qty: ${sale.Quantity}, Price: ${sale.Price}`,
      arrows: "to",
    }));
  
    setState((prevState) => ({
      ...prevState,
      graph: {
        nodes: prevState.graph.nodes,
        edges: [...prevState.graph.edges, ...salesEdges],
      },
    }));
  }, []);
  

  const { graph, events } = state;

  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    setIsClient(true);
  }, []);

  return isClient ? (
    <Graph
      graph={graph}
      options={options}
      events={events}
      style={{ height: "100vh" }}
    />
  ) : null;
};