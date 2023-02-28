import type { Meta, StoryObj } from '@storybook/svelte';

import Navbar from '$components/Navbar.svelte';

const meta = {
  title: 'Navbar',
  component: Navbar,
} satisfies Meta<Navbar>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    
  }
};

