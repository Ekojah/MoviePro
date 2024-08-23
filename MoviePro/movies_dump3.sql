-- MySQL dump 10.13  Distrib 5.7.24, for osx10.9 (x86_64)
--
-- Host: localhost    Database: movies
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Genres`
--

DROP TABLE IF EXISTS `Genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genres`
--

LOCK TABLES `Genres` WRITE;
/*!40000 ALTER TABLE `Genres` DISABLE KEYS */;
INSERT INTO `Genres` VALUES (1,'Drama'),(2,'Action'),(3,'Crime'),(4,'Adventure'),(5,'Comedy'),(6,'Animation'),(7,'Horror'),(8,'Mystery');
/*!40000 ALTER TABLE `Genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MovieGenres`
--

DROP TABLE IF EXISTS `MovieGenres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MovieGenres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `movie_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `moviegenres_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `Movies` (`id`),
  CONSTRAINT `moviegenres_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `Genres` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MovieGenres`
--

LOCK TABLES `MovieGenres` WRITE;
/*!40000 ALTER TABLE `MovieGenres` DISABLE KEYS */;
INSERT INTO `MovieGenres` VALUES (1,1,1),(2,2,1),(3,3,2),(4,4,3),(5,5,3),(6,6,1),(7,7,2),(8,8,3),(9,9,2),(10,10,4),(11,11,1),(12,12,1),(13,13,2),(14,14,2),(15,15,2),(16,16,2),(17,17,3),(18,18,1),(19,19,3),(20,20,2),(21,21,1),(22,22,3),(23,23,3),(24,24,1),(25,25,4),(26,26,5),(27,27,3),(28,28,2),(29,29,2),(30,30,4),(31,31,6),(32,32,1),(33,33,7),(34,34,1),(35,35,2),(36,36,6),(37,37,2),(38,38,3),(39,39,3),(40,40,3),(41,41,1),(42,42,1),(43,43,1),(44,44,6),(45,45,2),(46,46,5),(47,47,5),(48,48,2),(49,49,8);
/*!40000 ALTER TABLE `MovieGenres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `year` int DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `trailer_url` varchar(255) DEFAULT NULL,
  `poster_url` varchar(255) DEFAULT NULL,
  `punchline` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'The Shawshank Redemption',1994,9.3,'https://www.youtube.com/watch?v=PLl99DlL6b4',NULL,'Fear can hold you prisoner. Hope can set you free.'),(2,'The Godfather',1972,9.2,'https://www.youtube.com/watch?v=UaVTIH8mujA',NULL,'An offer you can\'t refuse.'),(3,'The Dark Knight',2008,9,'https://www.youtube.com/watch?v=EXeTwQWrcwY',NULL,'Why So Serious?'),(4,'The Godfather Part II',1974,9,'https://www.youtube.com/watch?v=9O1Iy9od7-A',NULL,'All the power on earth can\'t change destiny.'),(5,'12 Angry Men',1957,9,'https://www.youtube.com/watch?v=TEN-2uTi2c0',NULL,'Life Is In Their Hands -- Death Is On Their Minds!'),(6,'Schindler\'s List',1993,9,'https://www.youtube.com/watch?v=gG22XNhtnoY',NULL,'Whoever saves one life, saves the world entire.'),(7,'The Lord of the Rings: The Return of the King',2003,9,'https://www.youtube.com/watch?v=r5X-hFf6Bwo',NULL,'The eye of the enemy is moving.'),(8,'Pulp Fiction',1994,8.9,'https://www.youtube.com/watch?v=s7EdQ4FqbhY',NULL,'Girls like me don\'t make invitations like this to just anyone!'),(9,'The Lord of the Rings: The Fellowship of the Ring',2001,8.8,'https://www.youtube.com/watch?v=V75dMMIW2B4',NULL,'The Legend Comes to Life'),(10,'The Good, the Bad and the Ugly',1966,8.8,'https://www.youtube.com/watch?v=WCN5JJY_wiA',NULL,'They formed an alliance of hate to steal a fortune in dead man\'s gold'),(11,'Forrest Gump',1994,8.8,'https://www.youtube.com/watch?v=bLvqoHBptjg',NULL,'The story of a lifetime.'),(12,'Fight Club',1999,8.8,'https://www.youtube.com/watch?v=qtRKdVHc-cE',NULL,'How much can you know about yourself if you\'ve never been in a fight?'),(13,'The Lord of the Rings: The Two Towers',2002,8.8,'https://www.youtube.com/watch?v=LbfMDwc4azU',NULL,'A New Power Is Rising.'),(14,'Inception',2010,8.8,'https://www.youtube.com/watch?v=YoHD9XEInc0',NULL,'Your mind is the scene of the crime'),(15,'Star Wars: Episode V - The Empire Strikes Back',1980,8.7,'https://www.youtube.com/watch?v=JNwNXF9Y6kY',NULL,'The Adventure Continues...'),(16,'The Matrix',1999,8.7,'https://www.youtube.com/watch?v=vKQi3bBA1y8',NULL,'Free your mind'),(17,'Goodfellas',1990,8.7,'https://www.youtube.com/watch?v=2ilzidi_J8Q',NULL,'As far back as I can remember, I\'ve always wanted to be a gangster. -- Henry Hill, Brooklyn, N.Y. 1955.'),(18,'One Flew Over the Cuckoo\'s Nest',1975,8.7,'https://www.youtube.com/watch?v=OXrcDonY-B8',NULL,'If he\'s crazy, what does that make you?'),(19,'Se7en',1995,8.6,'https://www.youtube.com/watch?v=znmZoVkCjpI',NULL,'Long is the way, and hard, that out of hell leads up to light.'),(20,'Seven Samurai',1954,8.6,'https://www.youtube.com/watch?v=wJ1TOratCTo',NULL,'Will Take Its Place With the Seven Greatest Films of All Time!'),(21,'It\'s a Wonderful Life',1946,8.6,'https://www.youtube.com/watch?v=iLR3gZrU2Xo',NULL,'Frank Capra\'s...It\'s a Wonderful Life.'),(22,'The Silence of the Lambs',1991,8.6,'https://www.youtube.com/watch?v=6iB21hsprAQ',NULL,'Dr. Hannibal Lecter. Brilliant. Cunning. Psychotic. In his mind lies the clue to a ruthless killer. - Clarice Starling, FBI. Brilliant. Vulnerable. Alone. She must trust him to stop the killer.'),(23,'City of God',2002,8.6,'https://www.youtube.com/watch?v=dcUOO4Itgmw',NULL,'If you run, the beast will get you. If you stay, the beast will eat you'),(24,'Saving Private Ryan',1998,8.6,'https://www.youtube.com/watch?v=9CiW_DgxCnQ',NULL,'In the Last Great Invasion of the Last Great War, The Greatest Danger for Eight Men was Saving... One.'),(25,'Interstellar',2014,8.6,'https://www.youtube.com/watch?v=zSWdZVtXT7E',NULL,'Mankind was born on Earth. It was never meant to die here.'),(26,'Life Is Beautiful',1997,8.6,'https://www.youtube.com/watch?v=8CTjcVr9Iao',NULL,'An unforgettable fable that proves love, family and imagination conquer all. (Canadian one sheet)'),(27,'The Green Mile',1999,8.6,'https://www.youtube.com/watch?v=Ki4haFrqSrw',NULL,'Miracles do happen.'),(28,'Star Wars: Episode IV - A New Hope',1977,8.6,'https://www.youtube.com/watch?v=vZ734NWnAHA',NULL,'It\'s Back! The Force will be with you for three weeks only. (1979 Reissue Poster)'),(29,'Terminator 2: Judgment Day',1991,8.6,'https://www.youtube.com/watch?v=CRRlbK5w8AE',NULL,'It\'s nothing personal.'),(30,'Back to the Future',1985,8.5,'https://www.youtube.com/watch?v=qvsgGtivCgs',NULL,'He\'s the only kid ever to get into trouble before he was born. [UK]'),(31,'Spirited Away',2001,8.5,'https://www.youtube.com/watch?v=ByXuk9QqQkk',NULL,'The tunnel led Chihiro to a mysterious town.'),(32,'The Pianist',2002,8.5,'https://www.youtube.com/watch?v=BFwGqLa_oAo',NULL,'Music was his passion. Survival was his masterpiece.'),(33,'Psycho',1960,8.5,'https://www.youtube.com/watch?v=NG3-GlvKPcg',NULL,'The picture you MUST see from the beginning... Or not at all!... For no one will be seated after the start of... Alfred Hitchcock\'s greatest shocker Psycho.'),(34,'Parasite',2019,8.5,'https://www.youtube.com/watch?v=5xH0HfJHsaY',NULL,'Misplaced familyhood (Australia/New Zealand/Singapore)'),(35,'Léon: The Professional',1994,8.5,'https://www.youtube.com/watch?v=aNQqoExfQsg',NULL,'If you want the job done right, hire a professional.'),(36,'The Lion King',1994,8.5,'https://www.youtube.com/watch?v=o17MF9vnabg',NULL,'See it for the first time ever in 3D (2011 3D re-release)'),(37,'Gladiator',2000,8.5,'https://www.youtube.com/watch?v=P5ieIbInFpg',NULL,'Father of a murdered son, husband to a murdered wife and I shall have my vengeance in this life or the next'),(38,'American History X',1998,8.5,'https://www.youtube.com/watch?v=XfQYHqsiN5g',NULL,'His father taught him to hate. His friends taught him rage. His enemies gave him hope.'),(39,'The Departed',2006,8.5,'https://www.youtube.com/watch?v=r-MiSNsCdQ4',NULL,'Lies. Betrayal. Sacrifice. How far will you take it?'),(40,'The Usual Suspects',1995,8.5,'https://www.youtube.com/watch?v=x3t0Nc6fg7w',NULL,'The greatest trick the devil ever pulled was to convince the world he didn\'t exist'),(41,'The Prestige',2006,8.5,'https://www.youtube.com/watch?v=RLtaA9fFNXU',NULL,'A Friendship That Became a Rivalry.'),(42,'Whiplash',2014,8.5,'https://www.youtube.com/watch?v=7d_jQycdQGo',NULL,'The road to greatness can take you to the edge'),(43,'Casablanca',1942,8.5,'https://www.youtube.com/watch?v=MF7JH_54d8c',NULL,'Where Love Cuts as Deep as a Dagger!'),(44,'Grave of the Fireflies',1988,8.5,'https://www.youtube.com/watch?v=4vPeTSRd580',NULL,'imationDramaWar'),(45,'Harakiri',1962,8.6,'https://www.youtube.com/watch?v=gfABwM-Ppng',NULL,'The World Has Never Understood Why the Japanese Prefer Death to Dishonor! This Samurai Picture Provides The Answer!!'),(46,'The Intouchables',2011,8.5,'https://www.youtube.com/watch?v=34WIbmXkewU',NULL,'Sometimes you have to reach into someone else\'s world to find out what\'s missing in your own.'),(47,'Modern Times',1936,8.5,'https://www.youtube.com/watch?v=GLeDdzGUTq0',NULL,'He stands alone as the greatest entertainer of modern times! No one on earth can make you laugh as heartily or touch your heart as deeply...the whole world laughs, cries and thrills to his priceless genius!'),(48,'Once Upon a Time in the West',1968,8.5,'https://www.youtube.com/watch?v=c8CJ6L0I6W8',NULL,'There were three men in her life. One knew her past. One wanted her land. One wanted revenge.'),(49,'Rear Window',1954,8.5,'https://www.youtube.com/watch?v=m01YktiEZCw',NULL,'The Essential Hitchcock');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserLikes`
--

DROP TABLE IF EXISTS `UserLikes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserLikes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `movie_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `movie_id` (`movie_id`),
  CONSTRAINT `userlikes_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `userlikes_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `Movies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserLikes`
--

LOCK TABLES `UserLikes` WRITE;
/*!40000 ALTER TABLE `UserLikes` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserLikes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `google_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `google_id` (`google_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-20 15:56:21
