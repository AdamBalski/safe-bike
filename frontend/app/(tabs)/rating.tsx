import React, { Component, useState } from 'react';
import { Image, StyleSheet, Button, View, Text, Alert } from 'react-native';

import { HelloWave } from '@/components/HelloWave';
import ParallaxScrollView from '@/components/ParallaxScrollView';
import { ThemedText } from '@/components/ThemedText';
import { ThemedView } from '@/components/ThemedView';
import StarRating from 'react-native-star-rating-widget';

type RateProps = {
  rating: number;
  setRating: React.Dispatch<React.SetStateAction<number>>;
};

const RatingButtons = (props: RateProps) => {

  return (
      <StarRating
        rating={props.rating}
        onChange={props.setRating}
      />
  );
};

const Curr_Rate = (props: RateProps) => {
  return <Text style={styles.rateText}>Rate: {props.rating}!</Text>;
};

const SendRateButton = (props: RateProps) => {
  const PressButton = () => {
    Alert.alert(String(props.rating));
  }

    return (
      <View style={styles.container}>
        <View style={styles.buttonContainer}>
          <Button onPress={PressButton} title="Send your opinion" />
        </View>
      </View>
    );
}

export default function RatingScreen() {
  const rate : number = 0
  const [rating, setRating] = useState(0);
  
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#A1CEDC', dark: '#1D3D47' }}
      headerImage={
        <Image
          source={require('@/assets/images/partial-react-logo.png')}
          style={styles.reactLogo}
        />
      }>
      <ThemedView style={styles.titleContainer}>
        <ThemedText type="title">Rate your track!</ThemedText>
        <HelloWave />
      </ThemedView>
      <RatingButtons rating={rating} setRating={setRating} />
      <Curr_Rate rating={rating} setRating={setRating} />
      <SendRateButton rating={rating} setRating={setRating}/>
    </ParallaxScrollView>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
  },
  buttonContainer: {
    margin: 20,
  },
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
  rateText: {
    fontSize: 20
  }
});