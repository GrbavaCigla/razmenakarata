const config = {
  content: ["./src/**/*.{html,js,svelte,ts}"],

  theme: {
    extend: {},
  },

  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        light: {
          primary: "#ef4444",
          secondary: "#fb923c",
          accent: "#37CDBE",
          neutral: "#3D4451",
          "base-100": "#FFFFFF",
          info: "#3ABFF8",
          success: "#36D399",
          warning: "#FBBD23",
          error: "#F87272",
        },
      },
      {
        dark: {
          primary: "#ef4444",
          secondary: "#fb923c",
          accent: "#37CDBE",
          neutral: "#3D4451",
          "base-100": "#1f2937",
          info: "#3ABFF8",
          success: "#36D399",
          warning: "#FBBD23",
          error: "#F87272",
        },
      },
    ],
  },
};

module.exports = config;
