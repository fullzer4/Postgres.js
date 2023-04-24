import { View, Text, StyleSheet } from "react-native"

const app = () => {
    return(
        <View style={styles.container}>
            <Text>OpheliaAI</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#050505',
        alignItems: 'center',
        justifyContent: "space-between",
        paddingBottom: 25,
    }
})

export default app