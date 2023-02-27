import type { Meta, StoryObj } from '@storybook/svelte';

import Alert from '$components/Alert.svelte';

const meta = {
  title: 'Alert',
  component: Alert,
} satisfies Meta<Alert>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    title: "This is an example alert."
  }
};

