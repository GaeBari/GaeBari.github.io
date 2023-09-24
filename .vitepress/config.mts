import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "개발이하고싶어 아카이브",
  description:
    '"개발이하고싶어" 오픈채팅방에서 공유된 자료, 정보, 토론 내용을 정리하기 위한 아카이브 입니다.',
  cleanUrls: true,
  lastUpdated: true,

  // sitemap: {
  // hostname: 'https://example.com',
  // },

  rewrites: {
    "README.md": "index.md",
    "개발/README.md": "archive/dev.md",
    "운영/README.md": "archive/operation.md",
    "게임/README.md": "archive/game.md",
    "보안/README.md": "archive/security.md",
    "비개발/README.md": "archive/non-dev.md",
    "기타/README.md": "archive/etc.md",
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [{ text: "오픈채팅방", link: "https://open.kakao.com/o/gTMGkfjf" }],

    sidebar: [
      {
        text: "아카이브",
        base: "/archive/",
        items: [
          { text: "개발", link: "dev" },
          { text: "운영", link: "operation" },
          { text: "CS", link: "cs" },
          { text: "게임", link: "game" },
          { text: "보안", link: "security" },
          { text: "비개발", link: "non-dev" },
          { text: "기타", link: "etc" },
        ],
      },
      { text: "기여 방법", link: "how-to-contribute" },
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/GaeBari/archive" },
    ],
  },
});
